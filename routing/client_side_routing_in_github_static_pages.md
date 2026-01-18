For **GitHub Pages specifically**: when you hit /dashboard, it can show content at `/dashboard`**, but **only if you set it up in a specific way**. By default, GitHub Pages **does not support server-side rewrites**.

* * *

## What happens by default on GitHub Pages

If you deploy a SPA (React/Vue/etc.) and:

* You visit `/` → ✅ works
    
* You navigate to `/dashboard` **via client-side navigation** → ✅ works
    
* You **refresh** `/dashboard` or directly open `/dashboard` → ❌ **404 error**
    

Reason: GitHub Pages looks for a physical file at `/dashboard/index.html` and doesn’t find one.

* * *

## How to make `/dashboard` show content on GitHub Pages

### ✅ The 404 fallback technique (standard solution)

GitHub Pages serves `404.html` for _any unknown route_.  
So you exploit that behavior.

### Steps

1. **Create `404.html`**
    
2. Make it **identical to `index.html`**
    
3. Ensure your router uses **history mode**
    

Now the flow becomes:

```
/dashboard
→ GitHub Pages can’t find a file
→ serves 404.html
→ your SPA JS loads
→ client router renders /dashboard
```

Result:  
✅ `/dashboard` shows the correct content

* * *

## Example (React Router)

```jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";

<BrowserRouter>
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/dashboard" element={<Dashboard />} />
  </Routes>
</BrowserRouter>
```

With `404.html` in place, this works even on refresh.

* * *

## Important caveats (GitHub Pages)

### ⚠ Status code

* The response is still **404**, even though content renders
    
* Bad for SEO
    
* Acceptable for demos and internal tools
    

### ⚠ Subdirectory hosting

If your site is hosted at:

```
https://username.github.io/repo-name/
```

You must set:

* **React**: `homepage` in `package.json`
    
* **Router basename**:
    

```jsx
<BrowserRouter basename="/repo-name">
```

* * *

## Summary

| Action | Result on GitHub Pages |
| --- | --- |
| Direct visit `/dashboard` (no config) | ❌ 404 |
| Client-side navigation to `/dashboard` | ✅ |
| Direct visit `/dashboard` + `404.html` fallback | ✅ |
| Proper HTTP 200 rewrite | ❌ Not supported |

* * *

## Recommendation

If you **need clean 200 responses** and proper SPA routing without hacks:

* Use **Netlify**, **Vercel**, or **Cloudflare Pages**
    

If you want, tell me:

* Framework (React/Vue/etc.)
    
* Repo vs root domain  
    and I’ll give you an exact working config.