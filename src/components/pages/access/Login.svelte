<script>
  import { onMount } from 'svelte';
  import { navigate } from 'svelte-routing';

  let user = '';
  let password = '';

  onMount(() => {

  });

  const access = (event) => {
    event.preventDefault();
    console.log(user);
    console.log(password);
  }
</script>
<style></style>

<svelte:head>
	<title>Ingresar al Sistema</title>
</svelte:head>
<div class="container mt-5">
  <div class="row justify-content-center">
    <div class="col-md-6">
      <div class="card">
        <div class="card-header">
          <h3 class="text-center">Login</h3>
        </div>
        <div class="card-body">
          <form>
            <div class="mb-3">
              <label for="username" class="form-label">Username</label>
              <input type="text" class="form-control" id="username" required bind:value={user}>
            </div>
            <div class="mb-3">
              <label for="password" class="form-label">Password</label>
              <input type="password" class="form-control" id="password" required bind:value={password}>
            </div>
            <button  class="btn btn-primary w-100" on:click={access}>Login</button>
          </form>
          <div class="text-center mt-3">
            <a class="navbar-brand" href="/reset-password" on:click|preventDefault={() => {navigate('/reset-password')}}>Recuperar Contraseña</a>
            <span class="mx-2">|</span>
            <a class="navbar-brand" href="/sign-up" on:click|preventDefault={() => {navigate('/sign-up')}}>Crear Cuenta</a>
          </div>
        </div>
        <div class="card-footer text-center">
          <small>&copy; 2024 Your Brand</small>
        </div>
      </div>
    </div>
  </div>
</div>