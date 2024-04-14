console.log('loaded');

document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const response = await fetch(event.target.action, {
      method: 'POST',
      body: formData
    });
  
    if (response.ok) {
        // Create overlay
        const overlay = document.createElement('div');
        overlay.classList.add('overlay');
        document.body.appendChild(overlay);
      
        // Start animation
        overlay.animate([
          { clipPath: 'circle(75% at 50% 50%)' }, // Adjust starting size as needed
          { clipPath: 'circle(0% at 50% 50%)' }
        ], {
          duration: 300, // Animation duration in milliseconds
          direction: 'reverse', // Play the animation in reverse
          fill: 'forwards' // Keep the final state after animation completes
        }).onfinish = () => {
          window.location.href = '/home'; // Redirect after the animation
        };
      } else {
        // Show login error message
        document.getElementById('loginError').style.display = 'block';
      }
  });
  

  // Assuming Supabase JS is included in your project and initialized
  document.getElementById('googleSignInBtn').addEventListener('click', async () => {
    const { createClient } = supabase
    supabase = createClient('https://ogzyeworokewpqixuyxi.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9nenlld29yb2tld3BxaXh1eXhpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDgyNjczNDEsImV4cCI6MjAyMzg0MzM0MX0.QlO63kJIDv8itJ4LZE_zmM3pQN_7sLqvusRHUvBz5zA')


supabase.auth.signInWithOAuth({
        provider: 'google'

  })
  console.log(supabase)
});


