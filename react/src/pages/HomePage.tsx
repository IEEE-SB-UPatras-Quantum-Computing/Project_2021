import React from "react";
import "../static/styles/homePageStyle.scss";

export default function HomePage() {
  return (
    <div className='container home'>
      <div className="menu-bar">
          <a href="/superdense">Superdense</a>
          <a href="/teleportation">Teleportation</a>
          <a href="/cryptography">Cryptography</a>
      </div>
    </div>
  );
};
