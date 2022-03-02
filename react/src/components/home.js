import './components.css';
import './home.css';

function Home(props) {
    return (
        <section className='home'>
            {/* <h3>Home</h3> */}
            <div class="menu-bar">
                <a href="/superdense">Superdense</a>
                <a href="/teleportation">Teleportation</a>
                <a href="/cryptography">Cryptography</a>
            </div>
        </section>
    );
}

export default Home;
