// src/components/ContentItem.js
import React from 'react';

const ContentItem = ({ content }) => {
    return (
        <div>
            <h3>{content.title}</h3>
            <p>{content.description}</p>
        </div>
    );
};

export default ContentItem;