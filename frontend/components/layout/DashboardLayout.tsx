import Sidebar from "./Sidebar";
import Navbar from "./Navbar";

type Props = {
  children: React.ReactNode;
};

export default function DashboardLayout({
  children,
}: Props) {
  return (
    <div className="flex min-h-screen">
      <Sidebar />

      <div className="flex flex-1 flex-col">
        <Navbar />

        <main className="flex-1 p-6 bg-gray-50">
          {children}
        </main>
      </div>
    </div>
  );
}