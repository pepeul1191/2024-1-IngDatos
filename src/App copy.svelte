<script lang="ts">
	import { onMount } from 'svelte';
  import { 
		Button, 
		Offcanvas,  
		Collapse,
    NavbarToggler,
    NavbarBrand,
    Nav,
    Navbar,
    NavItem,
    NavLink,
    Dropdown,
    DropdownToggle,
    DropdownMenu,
    DropdownItem,
    OffcanvasHeader,
    OffcanvasBody,
  }  from 'sveltestrap';

  let isOpenOffCanvas = false;
	let isOpen = false;
	let isSideBarOpen = false;

  const toggleOffCanvas = () => {
    isOpenOffCanvas = !isOpenOffCanvas;
  };

	const handleUpdate = (event) => {
    isOpen = event.detail.isOpen;
  }

	const toggleSidebar = () => {
    isSideBarOpen = !isSideBarOpen;
  };
</script>

<Navbar color="light" light expand="md" container="">
  <NavbarBrand href="/">NavBar with md container</NavbarBrand>
  <NavbarToggler on:click={() => (isOpen = !isOpen)} />
  <Collapse {isOpen} navbar expand="md" on:update={handleUpdate}>
    <Nav class="ms-auto" navbar>
      <NavItem>
        <NavLink href="#components/">Components</NavLink>
      </NavItem>
      <NavItem>
        <NavLink href="https://github.com/sveltestrap/sveltestrap">GitHub</NavLink>
      </NavItem>
      <Dropdown nav inNavbar>
        <DropdownToggle nav caret>Options</DropdownToggle>
        <DropdownMenu end>
          <DropdownItem>Option 1</DropdownItem>
          <DropdownItem>Option 2</DropdownItem>
          <DropdownItem divider />
          <DropdownItem>Reset</DropdownItem>
        </DropdownMenu>
      </Dropdown>
    </Nav>
  </Collapse>
</Navbar>

<div class="sidebar {isOpen ? 'open' : 'closed'}">
  <button class="btn btn-primary toggle-btn" on:click={toggleSidebar}>
    {isSideBarOpen ? 'Close' : 'Open'} Sidebar
  </button>
  <Nav vertical>
    <NavItem>
      <NavLink href="/">Home</NavLink>
    </NavItem>
    <NavItem>
      <NavLink href="/about">About</NavLink>
    </NavItem>
    <NavItem>
      <NavLink href="/contact">Contact</NavLink>
    </NavItem>
  </Nav>
</div>

<div class="sidebar d-flex flex-column">
  <h4 class="text-white">Menu</h4>
  <ul class="nav flex-column">
    <li class="nav-item">
      <a class="nav-link active" href="#">Home</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Profile</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Messages</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Settings</a>
    </li>
  </ul>
</div>

<Button class="btn btn-primary toggle-button" on:click={() => isSidebarOpen = !isSidebarOpen}>
  <svg width="24" height="24" viewBox="0 0 24 24">
    <path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</Button>

<!-- Sidebar -->
<Collapse bind:isOpen={isSidebarOpen} class="sidebar">
  <h4 class="text-white">Menu</h4>
  <ul class="nav flex-column">
    <li class="nav-item">
      <a class="nav-link active" href="#">Home</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Profile</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Messages</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Settings</a>
    </li>
  </ul>
</Collapse>

<!-- Contenido principal -->
<div class="content">
  <Offcanvas bind:isOpen={isOpen} placement="start">
    <OffcanvasHeader toggle={() => isOpen = true} class="sidebar-header">
      <h5 class="offcanvas-title">Menu</h5>
    </OffcanvasHeader>
    <OffcanvasBody class="sidebar-body">
      <ul class="nav flex-column">
        <li class="nav-item">
          <a class="nav-link active" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Profile</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Messages</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Settings</a>
        </li>
      </ul>
    </OffcanvasBody>
  </Offcanvas>
  
  <div class="container" style="">
    <Button color="primary" on:click={toggleOffCanvas}>Open</Button>
  </div>
  
  <Offcanvas header="No Backdrop" isOpen={isOpenOffCanvas} toggle={toggleOffCanvas} backdrop={false} placement="end" style="width: 950px">
    Look ma, no backdrop.
  </Offcanvas>
</div>



<style>
  .sidebar {
    position: fixed;
    top: 0;
    left: 0;
    width: 250px;
    height: 100%;
    background: #343a40;
    color: #fff;
    padding: 1rem;
    transition: transform 0.3s ease;
  }
  .sidebar.closed {
    transform: translateX(-100%);
  }
  .sidebar.open {
    transform: translateX(0);
  }
  .toggle-btn {
    margin-bottom: 1rem;
  }
  .nav-link {
    color: #fff;
  }
  .nav-link:hover {
    color: #ccc;
  }

  body {
      display: flex;
    }
    .sidebar {
      width: 250px;
      height: 100vh;
      background-color: #343a40;
      padding: 10px;
    }
    .sidebar .nav-link {
      color: #fff;
    }
    .sidebar .nav-link.active {
      background-color: #495057;
    }
    .content {
      flex: 1;
      padding: 20px;
    }
</style>