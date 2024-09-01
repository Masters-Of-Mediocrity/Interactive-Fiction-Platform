import React from 'react';
import Header from '../components/Header';
import StoryList from '../components/StoryList';
import Footer from '../components/Footer';

const HomePage = () => (
  <div>
    <Header />
    <main>
      <h1>Welcome to Interactive Fiction</h1>
      <StoryList />
    </main>
    <Footer />
  </div>
);

export default HomePage;
