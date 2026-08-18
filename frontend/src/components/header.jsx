import React, { useState } from "react";
import "../styles/header.CSS";

const Header = () => {
    const [isOpen, setIsOpen] = useState(false);

    const toggleMenu = () => {
        setIsOpen(!isOpen);
    };

    return (
        <header className="header">
            {/* Left Corner: Logo */}
            <a href="/home" className="logo-link">
                <img src="/logo.png" alt="Logo" className="logo" />
            </a>

            {/* Middle: Search Bar (Desktop Only) */}
            <form className="search-container">
                <input 
                    type="search" 
                    placeholder="Search..." 
                    className="search-input" 
                />
            </form>

            {/* Right Corner: Desktop Nav Menu / Mobile Burger Icon */}
            <nav className={`nav ${isOpen ? "open" : ""}`}>
                <ul className="nav-list">
                    <li className="nav-item"><a href="/home">Home</a></li>
                    <li className="nav-item"><a href="/scores">Scores & Fixtures</a></li>
                    <li className="nav-item"><a href="/watch">Watch</a></li>
                    <li className="nav-item"><a href="/blog">Blog</a></li>
                    <li className="nav-item"><a href="/forums">Forums</a></li>
                </ul>
            </nav>

            {/* Right Corner: Burger Menu Button (Mobile Only) */}
            <button className="burger-menu" onClick={toggleMenu} aria-label="Toggle navigation">
                <span className={`bar ${isOpen ? "transform-top" : ""}`}></span>
                <span className={`bar ${isOpen ? "transform-middle" : ""}`}></span>
                <span className={`bar ${isOpen ? "transform-bottom" : ""}`}></span>
            </button>
        </header>
    );
};

export default Header;