/**
 * routes/gallery.js
 * -----------------
 * Public Gallery Routes
 * Version: v1
 */

const express = require('express');
const router = express.Router();
const galleryController = require('../controllers/galleryController');

/**
 * @route   GET /api/gallery
 * @desc    Get all approved projects for public gallery
 * @access  Public
 */
router.get('/', galleryController.getGallery);

/**
 * @route   GET /api/gallery/featured
 * @desc    Get featured projects
 * @access  Public
 */
router.get('/featured', galleryController.getFeaturedProjects);

/**
 * @route   GET /api/gallery/faculty/:faculty
 * @desc    Get projects by faculty
 * @access  Public
 */
router.get('/faculty/:faculty', galleryController.getProjectsByFaculty);

/**
 * @route   GET /api/gallery/technology/:technology
 * @desc    Get projects by technology
 * @access  Public
 */
router.get('/technology/:technology', galleryController.getProjectsByTechnology);

/**
 * @route   GET /api/gallery/:id
 * @desc    Get project details by ID
 * @access  Public
 */
router.get('/:id', galleryController.getProjectDetails);

/**
 * @route   GET /api/gallery/:id/similar
 * @desc    Get similar projects
 * @access  Public
 */
router.get('/:id/similar', galleryController.getSimilarProjects);

module.exports = router;