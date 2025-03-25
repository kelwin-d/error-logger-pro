import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
    return (
        <div>
            <h1>Welcome to Error Logger Pro</h1>
            <p>Track, analyze, and resolve errors faster.</p>
            <Link to="/dashboard">View Dashboard</Link>
        </div>
    );
}

export default Home;

