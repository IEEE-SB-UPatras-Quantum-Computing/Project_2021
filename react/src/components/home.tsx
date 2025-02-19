import React from 'react';
import './components.css';
import './home.css';

function Home(props: any) {
    return (
        <section className='home'>
            <div className="menu-bar">
                <a href="/superdense">Superdense</a>
                <a href="/teleportation">Teleportation</a>
                <a href="/cryptography">Cryptography</a>
            </div>
        </section>
    );
}

export default Home;
