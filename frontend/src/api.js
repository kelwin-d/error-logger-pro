const API_BASE_URL = "/api";

export const fetchErrors = async (page, query) => {
    const response = await fetch(`${API_BASE_URL}/errors?page=${page}&query=${query}`);
    return await response.json();
};

export const login = async (username, password) => {
    const response = await fetch(`${API_BASE_URL}/token`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `username=${username}&password=${password}`,
    });

    return await response.json();
};
