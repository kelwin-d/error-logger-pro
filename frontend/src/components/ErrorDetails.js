import React from 'react';

const ErrorList = ({ errors }) => (
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Message</th>
                <th>Severity</th>
                <th>Timestamp</th>
            </tr>
        </thead>
        <tbody>
            {errors.map(error => (
                <tr key={error.id}>
                    <td>{error.id}</td>
                    <td>{error.message}</td>
                    <td>{error.severity}</td>
                    <td>{error.timestamp}</td>
                </tr>
            ))}
        </tbody>
    </table>
);

export default ErrorList;
