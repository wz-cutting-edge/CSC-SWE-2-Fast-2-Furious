import React, { useState } from 'react';

const UserProfile = () => {
    // Initial user data
    const [user, setUser] = useState({
        name: 'John Doe',
        email: 'john.doe@example.com',
        bio: 'This is a sample bio.',
    });

    // Local state for form editing
    const [isEditing, setIsEditing] = useState(false);
    const [editedUser, setEditedUser] = useState({ ...user });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setEditedUser((prev) => ({ ...prev, [name]: value }));
    };

    const handleEdit = () => {
        setIsEditing(true);
    };

    const handleSave = () => {
        setUser(editedUser);
        setIsEditing(false);
    };

    return (
        <div className="user-profile">
            <h2>User Profile</h2>
            {isEditing ? (
                <div className="edit-form">
                    <label>
                        Name:
                        <input
                            type="text"
                            name="name"
                            value={editedUser.name}
                            onChange={handleChange}
                        />
                    </label>
                    <label>
                        Email:
                        <input
                            type="email"
                            name="email"
                            value={editedUser.email}
                            onChange={handleChange}
                        />
                    </label>
                    <label>
                        Bio:
                        <textarea
                            name="bio"
                            value={editedUser.bio}
                            onChange={handleChange}
                        />
                    </label>
                    <button onClick={handleSave}>Save</button>
                </div>
            ) : (
                <div className="profile-info">
                    <p><strong>Name:</strong> {user.name}</p>
                    <p><strong>Email:</strong> {user.email}</p>
                    <p><strong>Bio:</strong> {user.bio}</p>
                    <button onClick={handleEdit}>Edit Profile</button>
                </div>
            )}
        </div>
    );
};

export default UserProfile;