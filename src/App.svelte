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
  }  from 'sveltestrap';

  let isOpenOffCanvas = false;
	let isOpen = false;
	let isSideBarOpen = true;

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

<Navbar color="light" light expand="md" container="fluid">
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
<div class="container" style="margin-left: 250px;">
	<Button color="primary" on:click={toggleOffCanvas}>Open</Button>
</div>

<Offcanvas header="No Backdrop" isOpen={isOpenOffCanvas} toggle={toggleOffCanvas} backdrop={false} placement="end" style="width: 950px">
  Look ma, no backdrop.
</Offcanvas>

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
</style>