var calc_cache = [
  '/',
  '/templates/Login.html'
]

// self.addEventListener('install', e =>{
//     console.log("Installed!")
//     e.waitUntil(
//         caches.open("calculator-cache").then(cache =>{
//             return cache.addAll(calc_cache)
//         })
//     )
// })


// self.addEventListener('fetch', e => {
//     console.log(`Initiating fetch request for: ${e.request.url} `)
//     e.respondWith(
//         caches.match(e.request).then(response => {
//             return response || fetch(e.request);
//         })
//     )
// })
var staticCacheName = 'djangopwa-v1';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll(calc_cache);
    })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
  if (requestUrl.origin === location.origin) {
    if (requestUrl.pathname === '/') {
      event.respondWith(fetch(event.request, { redirect: 'follow' }));
      return;
    }
  }
  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});
