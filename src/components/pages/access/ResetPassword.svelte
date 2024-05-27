<script>
  import { onMount } from 'svelte';
  import { navigate } from 'svelte-routing';
  
  onMount(() => {

  });
</script>
<style></style>

<div class="container mt-5">
  <div class="row justify-content-center">
    <div class="col-md-6">
      <div class="card">
        <div class="card-header">
          <h3 class="text-center">Change Account Email</h3>
        </div>
        <div class="card-body">
          <form>
            <div class="mb-3">
              <label for="email" class="form-label">New Email Address</label>
              <input type="email" class="form-control" id="email" required>
            </div>
            <button type="submit" class="btn btn-primary w-100">Update Email</button>
          </form>
        </div>
        <div class="card-footer text-center">
          <small>&copy; 2024 Your Brand</small>
        </div>
      </div>
    </div>
  </div>
</div>