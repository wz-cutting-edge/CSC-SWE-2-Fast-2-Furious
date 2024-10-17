// src/components/Library.js
import React, { useState } from 'react';

const Library = () => {
    const [books, setBooks] = useState([
        { id: 1, title: '1984', author: 'George Orwell', year: 1949 },
        { id: 2, title: 'To Kill a Mockingbird', author: 'Harper Lee', year: 1960 },
    ]);
    
    const [newBook, setNewBook] = useState({
        title: '',
        author: '',
        year: '',
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setNewBook((prev) => ({ ...prev, [name]: value }));
    };

    const handleAddBook = (e) => {
        e.preventDefault();
        if (!newBook.title || !newBook.author || !newBook.year) return;
        
        const bookToAdd = { id: books.length + 1, ...newBook };
        setBooks((prev) => [...prev, bookToAdd]);
        setNewBook({ title: '', author: '', year: '' }); // Reset the form
    };

    return (
        <div className="library">
            <h2>Library Database</h2>
            
            <form onSubmit={handleAddBook}>
                <input
                    type="text"
                    name="title"
                    placeholder="Book Title"
                    value={newBook.title}
                    onChange={handleChange}
                    required
                />
                <input
                    type="text"
                    name="author"
                    placeholder="Author"
                    value={newBook.author}
                    onChange={handleChange}
                    required
                />
                <input
                    type="number"
                    name="year"
                    placeholder="Year Published"
                    value={newBook.year}
                    onChange={handleChange}
                    required
                />
                <button type="submit">Add Book</button>
            </form>

            <h3>Books List</h3>
            <ul>
                {books.map((book) => (
                    <li key={book.id}>
                        <strong>{book.title}</strong> by {book.author} ({book.year})
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Library;