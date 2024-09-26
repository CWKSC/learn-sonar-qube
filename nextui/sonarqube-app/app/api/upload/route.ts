/* eslint-disable no-console */
import fs from "fs";
import path from "path";
import { exec } from "child_process";
import { promisify } from "util";

import { v4 as uuidv4 } from "uuid";
import { NextRequest, NextResponse } from "next/server";

const execAsync = promisify(exec);

export async function POST(request: NextRequest) {
  const formData = await request.formData();
  const file = formData.get("file") as File | null;

  if (!file) {
    return NextResponse.json({ error: "No file uploaded" }, { status: 400 });
  }

  const bytes = await file.arrayBuffer();
  const buffer = Buffer.from(bytes);

  // Generate a unique ID for the upload
  const uniqueId = uuidv4();

  // Create a directory for the unique ID
  const uploadDir = path.join(process.cwd(), "uploads", uniqueId);

  if (!fs.existsSync(uploadDir)) {
    fs.mkdirSync(uploadDir, { recursive: true });
  }

  // Write the file to the unique ID directory
  const filePath = path.join(uploadDir, file.name);

  fs.writeFileSync(filePath, buffer);

  // Run SonarQube scanner Docker command
  try {
    const dockerCommand = `docker run \
      --rm \
      --network=host \
      -e SONAR_HOST_URL="http://localhost:9000" \
      -v "${uploadDir}:/usr/src" \
      -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=local-project -Dsonar.token=sqp_eb35ab63a86ef63585563776d0cc2a644b9c2239" \
      sonarsource/sonar-scanner-cli`;

    const { stdout, stderr } = await execAsync(dockerCommand);

    console.log("SonarQube scanner output:", stdout);
    if (stderr) console.error("SonarQube scanner error:", stderr);

    // Add a delay to allow SonarQube to process the results
    await new Promise((resolve) => setTimeout(resolve, 5000));

    // Fetch SonarQube analysis results
    const sonarqubeApiUrl =
      "http://localhost:9000/api/issues/list?project=local-project&resolved=false";
    const sonarqubeToken = "squ_5ef2d264b81be30de7da95e11bc053a8586dd645";

    const response = await fetch(sonarqubeApiUrl, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${sonarqubeToken}`,
      },
    });

    if (!response.ok) {
      throw new Error(
        `SonarQube API request failed with status ${response.status}`,
      );
    }

    const analysisResult = await response.json();

    // console.log("Analysis result:", analysisResult);

    return NextResponse.json(
      {
        message: "File uploaded, scanned, and analysis retrieved successfully",
        uniqueId,
        analysisResult,
      },
      { status: 200 },
    );
  } catch (error) {
    console.error("Error processing file or fetching analysis results:", error);

    return NextResponse.json(
      { error: "Error processing file or fetching analysis results" },
      { status: 500 },
    );
  }
}
