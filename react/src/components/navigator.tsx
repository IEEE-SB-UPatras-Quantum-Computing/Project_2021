import React from 'react';
import '../static/styles/navigator.css';

function NavBar(props: any) {
    function active(algorithm="") {
        return props.algorithm===algorithm?"active":"";
    }

    return (
        <nav id="navigator">
            <a className={"home-link " + active()} href="/" > Home </a>
            <div className="right navMenu">
                <a className={active("superdense")} href="/superdense" > Superdense </a>
                <a className={active("teleportation")} href="/teleportation" > Teleportation </a>
                <a className={active("cryptography")} href="/cryptography" > Quantum Cryptography </a>
                <div className="dot" />
            </div>
        </nav>
    );
}

export default NavBar;
