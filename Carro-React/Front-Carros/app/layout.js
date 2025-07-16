import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

import Menu from "./components/Menu.jsx"

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-eist-mono",
  subsets: ["latin"],
});

export const metadata = {
  title: "Simple CRUD",
  description: "simple crud app",
};
// Código comum entre as páginas (como um template)
// children é o conteúdo das páginas
export default function RootLayout({ children }) {
  return (
    <html lang="pt-br">
      <body className={`${geistSans.variable} ${geistMono.variable}`}>
        <Menu />
        {children}
      </body>
    </html>
  );
}
