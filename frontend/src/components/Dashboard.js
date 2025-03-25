import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function Dashboard() {
    const [errors, setErrors] = useState([]);

    useEffect(() => {
        fetch('/api/errors')
            .then(response => response.json())
            .then(data => setErrors(data));
    }, []);

    return (
        <div>
            <h1>Error Dashboard</h1>
            <ul>
                {errors.map(error => (
                    <li key={error.id}>
                        <Link to={`/error/${error.id}`}>
                            {error.message} (Severity: {error.severity})
                        </Link>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Dashboard;

