import { Outlet } from "react-router-dom";
import Header from "../components/header";
import Footer from "../components/footer";

const SiteLayout = () => {
  return (
    <div className="site-frame bg-white">
      <Header />
      <main className="flex-1 flex flex-col">
        <Outlet />
      </main>
      <Footer />
    </div>
  );
};

export default SiteLayout;
