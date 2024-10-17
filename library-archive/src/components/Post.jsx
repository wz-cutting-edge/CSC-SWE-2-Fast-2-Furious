// src/components/Post.js
import React from 'react';

const Post = ({ post, onLike, onDislike }) => {
    return (
        <div className="post">
            <p>{post.content}</p>
            <div className="interaction">
                <button onClick={() => onLike(post.id)}>Like</button>
                <span>{post.likes} Likes </span>
                <button onClick={() => onDislike(post.id)}>Dislike</button>
                <span>{post.dislikes} Dislikes</span>
            </div>
        </div>
    );
};

export default Post;
