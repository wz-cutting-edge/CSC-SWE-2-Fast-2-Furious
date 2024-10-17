import React, { useState, useEffect } from 'react';
import api from '../services/api';
import ContentItem from './ContentItem';

const Feed = () => {
    const [contents, setContents] = useState([]);

    useEffect(() => {
        api.get('contents/')
            .then(response => setContents(response.data))
            .catch(error => console.error('Error fetching content:', error));
    }, []);

    return (
        <div>
            <h2>User Feed</h2>
            {contents.map(content => (
                <ContentItem key={content.id} content={content} />
            ))}
        </div>
    );
};

export default Feed;