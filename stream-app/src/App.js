
//Create an react page to fetch and display the streaming data from streamdata.py

import React, { useEffect,useState } from 'react';
import './App.css';

function SSEComponent() {
  return (
    <div className='content'>
      <header className='header-content'>
        <h1>Stream Data</h1>
      </header>
      <div className='header-task'>
        <h1>Camera 1</h1>
      </div>

      <div className='video-player'>
        <img src="http://localhost:5000/video" alt="Video Stream" />
        <br/>
      </div> 
      
    </div>

  );
}

export default SSEComponent;
