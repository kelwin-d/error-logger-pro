import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import ErrorDetails from './components/ErrorDetails';
import NotFound from './components/NotFound';
import AdminDashboard from './pages/AdminDashboard';
import Home from './pages/Home';
import Login from './pages/Login';

const App = () => {
    const token = localStorage.getItem('token');

    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/error/:id" element={<ErrorDetails />} />
                <Route path="/login" element={<Login />} />
                {token && <Route path="/admin-dashboard" element={<AdminDashboard />} />}
                <Route path="*" element={<NotFound />} />
            </Routes>
        </Router>
    );
};

export default App;

