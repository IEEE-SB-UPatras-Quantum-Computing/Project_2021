import React from 'react';
import {AppRoutes} from "../../constants/appRoutes.ts";

function NavBar(props: any) {
    function active(algorithm="") {
        return props.algorithm===algorithm ? "active" : "";
    }

    return (
        <nav id="navigator">
            <a className={"home-link " + active()} href={AppRoutes.ROOT} > Home </a>
            <div className="right navMenu">
                <a className={active("superdense")} href={AppRoutes.SUPERDENSE} > Superdense </a>
                <a className={active("teleportation")} href={AppRoutes.TELEPORTATION} > Teleportation </a>
                <a className={active("key-distribution")} href={AppRoutes.QKD} > Quantum Key Distribution </a>
                <div className="dot" />
            </div>
        </nav>
    );
}

export default NavBar;
