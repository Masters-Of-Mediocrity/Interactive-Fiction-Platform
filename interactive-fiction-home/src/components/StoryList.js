import React, { useEffect, useState } from 'react';
import { fetchStories } from '../services/api';

const StoryList = () => {
  const [stories, setStories] = useState([]);

  useEffect(() => {
    const getStories = async () => {
      const stories = await fetchStories();
      setStories(stories);
    };

    getStories();
  }, []);

  return (
    <section>
      <h2>Explore Stories</h2>
      <ul>
        {stories.map((story) => (
          <li key={story.id}>
            <h3>{story.title}</h3>
            <p>{story.description}</p>
            <small>By {story.author.username}</small>
          </li>
        ))}
      </ul>
    </section>
  );
};

export default StoryList;
