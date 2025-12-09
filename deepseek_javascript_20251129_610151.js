/**
 * routes/userRoutes.js
 * -----------------
 * User Management Routes
 * Version: v1
 */

const express = require('express');
const { body } = require('express-validator');
const router = express.Router();
const userController = require('../controllers/userController');
const authMiddleware = require('../middleware/authMiddleware');
const validateRequest = require('../middleware/validateRequest');
const authorize = require('../middleware/authorize');

// Validation rules
const userValidation = [
  body('email').isEmail().normalizeEmail(),
  body('name').notEmpty().trim().isLength({ min: 2, max: 100 }),
  body('faculty').optional().trim()
];

// Public routes
router.post(
  '/',
  userValidation,
  validateRequest,
  userController.createUser
);

// Protected routes (require authentication)
router.use(authMiddleware);

/**
 * @route   GET /api/users
 * @desc    Get all users (with pagination)
 * @access  Private
 */
router.get('/', userController.getAllUsers);

/**
 * @route   GET /api/users/profile
 * @desc    Get current user profile
 * @access  Private
 */
router.get('/profile', userController.getCurrentUser);

/**
 * @route   GET /api/users/:id
 * @desc    Get user by ID
 * @access  Private
 */
router.get('/:id', userController.getUserById);

/**
 * @route   PUT /api/users/profile
 * @desc    Update current user profile
 * @access  Private
 */
router.put(
  '/profile',
  userValidation,
  validateRequest,
  userController.updateProfile
);

/**
 * @route   PUT /api/users/:id
 * @desc    Update user (Admin only)
 * @access  Private (Admin)
 */
router.put(
  '/:id',
  authorize('admin'),
  userValidation,
  validateRequest,
  userController.updateUser
);

/**
 * @route   DELETE /api/users/:id
 * @desc    Delete user (Admin only)
 * @access  Private (Admin)
 */
router.delete(
  '/:id',
  authorize('admin'),
  userController.deleteUser
);

/**
 * @route   PATCH /api/users/:id/role
 * @desc    Update user role (Admin only)
 * @access  Private (Admin)
 */
router.patch(
  '/:id/role',
  authorize('admin'),
  userController.updateUserRole
);

module.exports = router;