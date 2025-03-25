import React, { useEffect, useState } from 'react';
import ErrorList from '../components/ErrorList';
import Pagination from '../components/Pagination';
import SearchBar from '../components/SearchBar';
import { fetchErrors } from '../api';

const AdminDashboard = () => {
    const [errors, setErrors] = useState([]);
    const [page, setPage] = useState(1);
    const [query, setQuery] = useState('');

    useEffect(() => {
        fetchErrors(page, query).then(setErrors);
    }, [page, query]);

    return (
        <div>
            <h1>Error Logger Dashboard</h1>
            <SearchBar onSearch={setQuery} />
            <ErrorList errors={errors} />
            <Pagination
                currentPage={page}
                totalPages={5}
                onPageChange={setPage}
            />
        </div>
    );
};

export default AdminDashboard;
