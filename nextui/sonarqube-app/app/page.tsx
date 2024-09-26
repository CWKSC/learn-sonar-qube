"use client";

import { Link } from "@nextui-org/link";
import { Snippet } from "@nextui-org/snippet";
import { Code } from "@nextui-org/code";
import { button as buttonStyles } from "@nextui-org/theme";
import { Button } from "@nextui-org/button";
import { useRef, useState } from "react";
import {
  Table,
  TableHeader,
  TableColumn,
  TableBody,
  TableRow,
  TableCell,
} from "@nextui-org/table";

import { siteConfig } from "@/config/site";
import { title, subtitle } from "@/components/primitives";
import { GithubIcon } from "@/components/icons";

export default function Home() {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [isUploading, setIsUploading] = useState(false);
  const [uploadStatus, setUploadStatus] = useState<string | null>(null);
  const [analysisResult, setAnalysisResult] = useState<any>(null);

  const handleUploadClick = () => {
    fileInputRef.current?.click();
  };

  const handleFileChange = async (
    event: React.ChangeEvent<HTMLInputElement>,
  ) => {
    const selectedFile = event.target.files?.[0];

    if (selectedFile) {
      setIsUploading(true);
      setUploadStatus(null);

      try {
        await uploadFileToServer(selectedFile);
        setUploadStatus("File uploaded successfully!");
      } catch (error) {
        // eslint-disable-next-line no-console
        console.error("Error uploading file:", error);
        setUploadStatus("Error uploading file. Please try again.");
      } finally {
        setIsUploading(false);
      }
    }
  };

  const uploadFileToServer = async (file: File) => {
    const formData = new FormData();

    formData.append("file", file);

    const response = await fetch("/api/upload", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("File upload failed");
    }

    const result = await response.json();

    setAnalysisResult(result.analysisResult);
  };

  return (
    <section className="flex flex-col items-center justify-center gap-4 py-8 md:py-10">
      <div className="inline-block max-w-xl text-center justify-center">
        <span className={title()}>Make&nbsp;</span>
        <span className={title({ color: "violet" })}>beautiful&nbsp;</span>
        <br />
        <span className={title()}>
          websites regardless of your design experience.
        </span>
        <div className={subtitle({ class: "mt-4" })}>
          Beautiful, fast and modern React UI library.
        </div>
      </div>

      <div className="mt-8">
        <Button
          color="primary"
          isLoading={isUploading}
          size="lg"
          onPress={handleUploadClick}
        >
          {isUploading ? "Uploading..." : "Upload"}
        </Button>
        <input
          ref={fileInputRef}
          style={{ display: "none" }}
          type="file"
          onChange={handleFileChange}
        />
        {uploadStatus && (
          <p
            className={`mt-2 ${uploadStatus.includes("Error") ? "text-red-500" : "text-green-500"}`}
          >
            {uploadStatus}
          </p>
        )}
      </div>

      <div className="flex gap-3">
        <Link
          isExternal
          className={buttonStyles({
            color: "primary",
            radius: "full",
            variant: "shadow",
          })}
          href={siteConfig.links.docs}
        >
          Documentation
        </Link>
        <Link
          isExternal
          className={buttonStyles({ variant: "bordered", radius: "full" })}
          href={siteConfig.links.github}
        >
          <GithubIcon size={20} />
          GitHub
        </Link>
      </div>

      <div className="mt-8">
        <Snippet hideCopyButton hideSymbol variant="bordered">
          <span>
            Get started by editing <Code color="primary">app/page.tsx</Code>
          </span>
        </Snippet>
      </div>

      {analysisResult && (
        <div className="mt-8 w-full max-w-4xl">
          <h2 className={title({ size: "sm" })}>Analysis Results</h2>
          <Table aria-label="SonarQube Analysis Results">
            <TableHeader>
              <TableColumn>Severity</TableColumn>
              <TableColumn>Type</TableColumn>
              <TableColumn>Message</TableColumn>
            </TableHeader>
            <TableBody>
              {analysisResult.issues.map((issue: any, index: number) => (
                <TableRow key={index}>
                  <TableCell>{issue.severity}</TableCell>
                  <TableCell>{issue.type}</TableCell>
                  <TableCell>{issue.message}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
          <div className="mt-4">
            <p>Total Issues: {analysisResult.total}</p>
            <p>Project: {analysisResult.project}</p>
          </div>
        </div>
      )}
    </section>
  );
}
