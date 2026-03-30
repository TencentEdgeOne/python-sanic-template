import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Sanic + EdgeOne Pages",
  description: "Deploy high-performance async Sanic applications as serverless functions on EdgeOne Pages. Build fast with Python async/await.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en-US">
      <head>
        <link rel="icon" href="/sanic-favicon.svg" />
      </head>
      <body
        className="antialiased"
      >
        {children}
      </body>
    </html>
  );
}
