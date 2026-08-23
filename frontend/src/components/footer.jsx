import { Link } from "react-router-dom";

const Footer = () => {
  return (
    <footer className="border-t border-[var(--border)] mt-auto">
      <div className="max-w-5xl mx-auto px-6 py-6 flex flex-col sm:flex-row items-center justify-between gap-3 text-sm text-[var(--text)]">
        <p>&copy; {new Date().getFullYear()} Gira Sports. All rights reserved.</p>
        <nav className="flex items-center gap-5">
          <Link to="/privacy" className="hover:text-[var(--accent)] transition-colors">Privacy Policy</Link>
          <Link to="/terms" className="hover:text-[var(--accent)] transition-colors">Terms of Service</Link>
          <Link to="/contact" className="hover:text-[var(--accent)] transition-colors">Contact Us</Link>
        </nav>
      </div>
    </footer>
  );
};

export default Footer;