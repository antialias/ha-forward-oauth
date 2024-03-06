self.addEventListener('fetch', event => {
  // This implements a network-only strategy
  event.respondWith(fetch(event.request));
});
