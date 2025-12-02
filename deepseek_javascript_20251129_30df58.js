/**
 * routes/index.js
 * -----------------
 * Centralized API Route Management
 * Version: v1
 */

const express = require('express');
const router = express.Router();

// Import route modules
const authRoutes = require('./auth');
const projectsRoutes = require('./projects');
const galleryRoutes = require('./gallery');
const analyticsRoutes = require('./analytics');
const userRoutes = require('./userRoutes');

// API Route Registration
router.use('/auth', authRoutes);
router.use('/projects', projectsRoutes);
router.use('/gallery', galleryRoutes);
router.use('/analytics', analyticsRoutes);
router.use('/users', userRoutes);

// API Health Check
router.get('/health', (req, res) => {
  res.status(200).json({
    success: true,
    message: 'UCU Innovators Hub API v1 is operational',
    timestamp: new Date().toISOString(),
    version: 'v1.0.0'
  });
});

// API Info Endpoint
router.get('/info', (req, res) => {
  res.json({
    api: 'UCU Innovators Hub API',
    version: 'v1.0.0',
    description: 'University Project Management System',
    endpoints: {
      auth: '/api/auth',
      projects: '/api/projects',
      gallery: '/api/gallery',
      analytics: '/api/analytics',
      users: '/api/users'
    }
  });
});

module.exports = router;