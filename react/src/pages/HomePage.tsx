import React from "react";
import "../static/styles/homePageStyle.scss";
import {AppRoutes} from "../constants/appRoutes.ts";

export default function HomePage() {
  return (
    <div className='container home'>
      <div className="menu-bar">
          <a href={AppRoutes.SUPERDENSE}>Superdense</a>
          <a href={AppRoutes.TELEPORTATION}>Teleportation</a>
          <a href={AppRoutes.QKD}>Quantum Key Distribution</a>
      </div>
    </div>
  );
};
