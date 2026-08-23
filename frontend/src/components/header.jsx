import { useState } from "react";
import { Link, NavLink } from "react-router-dom";
import logo from "../assets/logo.png";
import "../styles/header.css";

const NAV_LINKS = [
    { to: "/home", label: "Home" },
    { to: "/scores", label: "Scores & Fixtures" },
    { to: "/watch", label: "Watch" },
    { to: "/blog", label: "Blog" },
    { to: "/forums", label: "Forums" },
];

const Header = () => {
    const [isOpen, setIsOpen] = useState(false);

    const toggleMenu = () => {
        setIsOpen((open) => !open);
    };

    const closeMenu = () => setIsOpen(false);

    return (
        <header className="header">
            {/* Left Corner: Logo */}
            <Link to="/home" className="logo-link" onClick={closeMenu}>
                <img src={logo} alt="Gira Sports" className="logo" />
            </Link>

            {/* Middle: Search Bar (Desktop Only) */}
            <form className="search-container" onSubmit={(e) => e.preventDefault()}>
                <input
                    type="search"
                    placeholder="Search..."
                    className="search-input"
                />
            </form>

            {/* Right Corner: Desktop Nav Menu / Mobile Burger Icon */}
            <nav className={`nav ${isOpen ? "open" : ""}`}>
                <ul className="nav-list">
                    {NAV_LINKS.map(({ to, label }) => (
                        <li className="nav-item" key={to}>
                            <NavLink
                                to={to}
                                onClick={closeMenu}
                                className={({ isActive }) => (isActive ? "active" : undefined)}
                            >
                                {label}
                            </NavLink>
                        </li>
                    ))}
                </ul>
            </nav>

            {/* Right Corner: Burger Menu Button (Mobile Only) */}
            <button className="burger-menu" onClick={toggleMenu} aria-label="Toggle navigation" aria-expanded={isOpen}>
                <span className={`bar ${isOpen ? "transform-top" : ""}`}></span>
                <span className={`bar ${isOpen ? "transform-middle" : ""}`}></span>
                <span className={`bar ${isOpen ? "transform-bottom" : ""}`}></span>
            </button>
        </header>
    );
};

export default Header;