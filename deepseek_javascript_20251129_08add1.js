/**
 * routes/projects.js
 * -----------------
 * Project Management Routes
 * Version: v1
 */

const express = require('express');
const { body } = require('express-validator');
const router = express.Router();
const projectController = require('../controllers/projectController');
const authMiddleware = require('../middleware/authMiddleware');
const validateRequest = require('../middleware/validateRequest');
const authorize = require('../middleware/authorize');

// Validation rules
const projectValidation = [
  body('title').notEmpty().trim().isLength({ min: 3, max: 200 }),
  body('description').notEmpty().trim().isLength({ min: 10 }),
  body('faculty').notEmpty().trim(),
  body('technologies').isArray({ min: 1 })
];

// Public routes
router.get('/', projectController.getAllProjects);
router.get('/:id', projectController.getProjectById);

// Protected routes (require authentication)
router.use(authMiddleware); // All routes below require auth

/**
 * @route   POST /api/projects
 * @desc    Create new project
 * @access  Private
 */
router.post(
  '/',
  projectValidation,
  validateRequest,
  projectController.createProject
);

/**
 * @route   GET /api/projects/my/projects
 * @desc    Get current user's projects
 * @access  Private
 */
router.get('/my/projects', projectController.getMyProjects);

/**
 * @route   PUT /api/projects/:id
 * @desc    Update project
 * @access  Private (Project Owner or Admin)
 */
router.put(
  '/:id',
  projectValidation,
  validateRequest,
  authorize('project'),
  projectController.updateProject
);

/**
 * @route   DELETE /api/projects/:id
 * @desc    Delete project
 * @access  Private (Project Owner or Admin)
 */
router.delete(
  '/:id',
  authorize('project'),
  projectController.deleteProject
);

/**
 * @route   PATCH /api/projects/:id/status
 * @desc    Update project status (Admin only)
 * @access  Private (Admin)
 */
router.patch(
  '/:id/status',
  authorize('admin'),
  projectController.updateProjectStatus
);

module.exports = router;