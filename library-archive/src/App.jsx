import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Feed from './components/Feed.jsx';
import UserProfile from './components/UserProfile.jsx';
import './App.css'; // Custom styles

const App = () => {
    return (
        <Router>
            <div className="app-container">
                <nav className="navbar">
                    <div className="navbar-brand">
                        <Link to="/" className="navbar-logo">Library Archive</Link>
                    </div>
                    <ul className="navbar-menu">
                        <li><Link to="/">Home</Link></li>
                        <li><Link to="/profile">Profile</Link></li>
                    </ul>
                </nav>
                <main className="main-content">
                    <Routes>
                        <Route path="/" element={<Feed />} />
                        <Route path="/profile" element={<UserProfile />} />
                    </Routes>
                </main>
                <footer className="footer">
                    <p>&copy; 2024 LibraryArchiveApp. All rights reserved.</p>
                </footer>
            </div>
        </Router>
    );
};

export default App;