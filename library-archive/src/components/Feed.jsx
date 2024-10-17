
// src/components/Feed.js
import React, { useState } from 'react';
import Post from './Post';

const Feed = () => {
    // Sample data for posts
    const [posts, setPosts] = useState([
        { id: 1, content: 'Post 1', likes: 0, dislikes: 0 },
        { id: 2, content: 'Post 2', likes: 0, dislikes: 0 },
        { id: 3, content: 'Post 3', likes: 0, dislikes: 0 },
    ]);

    const handleLike = (id) => {
        setPosts((prevPosts) =>
            prevPosts.map((post) =>
                post.id === id ? { ...post, likes: post.likes + 1 } : post
            )
        );
    };

    const handleDislike = (id) => {
        setPosts((prevPosts) =>
            prevPosts.map((post) =>
                post.id === id ? { ...post, dislikes: post.dislikes + 1 } : post
            )
        );
    };

    return (
        <div className="feed">
            {posts.map((post) => (
                <Post
                    key={post.id}
                    post={post}
                    onLike={handleLike}
                    onDislike={handleDislike}
                />
            ))}
        </div>
    );
};

export default Feed;