<script lang="ts">
import { onMount } from 'svelte';
import { Router, Route } from 'svelte-routing';
import Sidebar from '../widgets/Sidebar.svelte';
import Navbar from '../widgets/Navbar.svelte';
import ThemeToggle from '../widgets/ThemeToggle.svelte';
import Footer from '../widgets/Footer.svelte';
import Home from '../pages/app/Home.svelte';
import Level from '../pages/app/Level.svelte';
import Contact from '../pages/app/Contact.svelte';

const toggleRootClass = () => {
  const current = document.documentElement.getAttribute('data-bs-theme');
  const inverted = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-bs-theme', inverted);
}

const toggleLocalStorage = () => {
  if (isLight()) {
    localStorage.removeItem('light');
  } else {
    localStorage.setItem('light', 'set');
  }
}

const isLight = () => {
  return localStorage.getItem('light');
}

onMount(() => {
  const sidebarToggle = document.querySelector('#sidebar-toggle');
  if (sidebarToggle) {
    sidebarToggle.addEventListener('click', () => {
      document.querySelector('#sidebar').classList.toggle('collapsed');
    });
  }

  const themeToggle = document.querySelector('.theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      toggleLocalStorage();
      toggleRootClass();
    });
  }

  if (isLight()) {
    toggleRootClass();
  }
});
</script>

<style></style>

<div class="wrapper">
  <Sidebar />
  <div class="main">
    <Navbar />
    <main class="content px-3 py-2">
      <div class="container-fluid">
        <Router>
          <Route path="/" component={Home} />
          <Route path="/level" component={Level} />
          <Route path="/contact" component={Contact} />
        </Router>
      </div>
    </main>
    <ThemeToggle />
    <Footer />
  </div>
</div>

