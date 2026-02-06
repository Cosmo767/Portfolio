# Data Science & Web Development Portfolio

A modern, colorful portfolio website showcasing your data science projects, blog posts, resume, and contact information.

## Features

✨ **Modern Design**
- Colorful gradient accents
- Smooth animations and transitions
- Responsive layout (mobile, tablet, desktop)
- Dark/light theme toggle

🎨 **Sections**
- Hero section with animated background
- About section with skills
- Featured projects grid
- Blog posts showcase
- Resume/Experience section
- Contact form

⚡ **Interactive Elements**
- Smooth scrolling navigation
- Active nav link highlighting
- Floating card animations
- Scroll-triggered animations
- Form validation and submission

## Quick Start

### Option 1: Deploy to Netlify (Recommended)

1. **Create a Netlify account** at https://netlify.com
2. **Drag and drop** this folder into Netlify's deploy zone
3. Your site is live! Netlify will give you a URL like `your-site.netlify.app`
4. (Optional) Add a custom domain in Netlify settings

### Option 2: Deploy to GitHub Pages

1. **Create a GitHub account** if you don't have one
2. **Create a new repository** named `your-username.github.io`
3. **Upload these files** to the repository:
   - index.html
   - styles.css
   - script.js
4. **Enable GitHub Pages**:
   - Go to repository Settings → Pages
   - Source: Deploy from branch → main
5. Your site will be live at `https://your-username.github.io`

### Option 3: Deploy to Vercel

1. **Create a Vercel account** at https://vercel.com
2. **Import your project** from GitHub or drag and drop the folder
3. Click "Deploy"
4. Your site is live instantly!

## Customization Guide

### 1. Personal Information

Edit `index.html` and replace:

```html
<!-- Line 6: Change the page title -->
<title>Your Name - Data Science & Web Development Portfolio</title>

<!-- Line 13: Update your name -->
<div class="logo">Your Name</div>

<!-- Lines 28-29: Update the hero title and subtitle -->
<h1 class="hero-title">...</h1>
<p class="hero-subtitle">...</p>

<!-- Lines 36-42: Update your social links -->
<a href="https://github.com/yourusername" target="_blank">
<a href="https://linkedin.com/in/yourusername" target="_blank">

<!-- Line 264: Update your email -->
<a href="mailto:your.email@example.com" class="contact-method">
```

### 2. About Section

Update lines 68-88 in `index.html` with:
- Your bio/introduction
- Your skills in the skill tags

### 3. Projects

For each project (lines 94-183), update:
- Project title
- Project description
- Technologies used (tags)
- Project and GitHub links
- Change the gradient color for variety

### 4. Blog Posts

Update blog cards (lines 192-230) with:
- Article titles
- Publication dates
- Descriptions
- Links to actual blog posts

### 5. Resume

Update lines 239-265 with:
- Your work experience
- Education
- Add more sections as needed

### 6. Colors & Theme

Edit `styles.css` to customize colors:

```css
/* Lines 2-6: Main gradients */
--primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
--secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
--accent-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
```

### 7. Contact Form

**Important:** The contact form currently logs to console. To make it functional:

#### Option A: Use Netlify Forms (Easiest)
```html
<!-- Add to the form tag in index.html -->
<form class="contact-form" id="contactForm" name="contact" method="POST" data-netlify="true">
    <input type="hidden" name="form-name" value="contact">
    <!-- rest of form fields -->
</form>
```

#### Option B: Use Formspree
1. Sign up at https://formspree.io
2. Get your form endpoint
3. Update the form in `script.js`:
```javascript
const response = await fetch('https://formspree.io/f/YOUR_FORM_ID', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(formData)
});
```

#### Option C: Use Web3Forms
1. Get API key from https://web3forms.com
2. Add hidden input to form:
```html
<input type="hidden" name="access_key" value="YOUR_ACCESS_KEY">
```

## Adding Your Resume PDF

1. Create/export your resume as `resume.pdf`
2. Place it in the same folder as `index.html`
3. The download button will work automatically

## File Structure

```
portfolio/
├── index.html      # Main HTML file
├── styles.css      # All styling
├── script.js       # JavaScript functionality
├── resume.pdf      # Your resume (add this)
└── README.md       # This file
```

## Adding a Blog

Your current portfolio links to blog posts. Here are options:

1. **Medium/Dev.to** - Write on these platforms and link to them
2. **Separate Blog Site** - Use Hugo, Jekyll, or Gatsby
3. **Integrated Blog** - Create `blog/` folder with individual HTML pages
4. **Headless CMS** - Use Contentful, Sanity, or Strapi

## Next Steps: Adding Dynamic Features

Once you're comfortable, consider adding:

### Data Visualizations
```html
<!-- Add D3.js -->
<script src="https://d3js.org/d3.v7.min.js"></script>
```

### Interactive Demos
- Embed Jupyter notebooks with nbviewer
- Create interactive charts with Plotly.js
- Build ML demos with TensorFlow.js

### Analytics
```html
<!-- Add Google Analytics to track visitors -->
<!-- Or use privacy-friendly alternatives like Plausible -->
```

## Troubleshooting

**Issue: Styles not loading**
- Check that all three files (HTML, CSS, JS) are in the same folder
- Ensure file names match exactly (case-sensitive)

**Issue: Contact form not working**
- The default form just logs to console
- Follow steps above to connect to a form service

**Issue: Theme toggle not working**
- Clear browser cache
- Check browser console for errors

## Resources for Learning

- **Web Development**: MDN Web Docs, freeCodeCamp
- **Data Visualization**: D3.js documentation, Observable
- **React (next step)**: React official tutorial
- **Deployment**: Netlify docs, Vercel docs

## Support

If you run into issues:
1. Check the browser console (F12) for errors
2. Validate HTML at https://validator.w3.org
3. Validate CSS at https://jigsaw.w3.org/css-validator/

## License

Feel free to use this template for your own portfolio! No attribution needed.

---

**Ready to deploy?** Choose one of the deployment options above and get your portfolio live in under 5 minutes! 🚀
