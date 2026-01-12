# brand-image-analysis
# Tech Stack: 
Python, TensorFlow/Keras, YOLOv7, Google Cloud Vision API, AutoML Vision, Power BI, Git

# 📌 Overview

An end-to-end computer vision & analytics project that studies how image-based posting strategies used by brands on social media impact consumer engagement (likes, comments, shares). The system detects brand logos and visual elements in images and correlates them with engagement metrics across brand categories.

This repository is designed to be production-aligned, resume-ready, and recruiter-friendly.

# 🎯 Objectives

Detect brand logos and key objects in social media images

Analyze the relationship between logo presence and engagement

Compare performance across brand categories (Fashion, FMCG, Tech, etc.)

Present insights through interactive dashboards

# 🧠 Solution Architecture
Data Collection

~10,000 public social media images

Engagement metrics: likes, comments, shares

Custom-labeled subset for logo/object detection

# Computer Vision Models

YOLOv7 – Real-time logo & object detection

ResNet-50 – Visual feature extraction

Google Cloud Vision API – Label & logo recognition

AutoML Vision – Brand-specific logo classification

# Training & Evaluation

Fine-tuned YOLOv7 on brand logo dataset

Evaluated using mAP, precision, recall

Benchmarked inference latency for deployment readiness

# Analytics & Insights

Merged CV outputs with engagement data

Performed correlation & category-wise analysis

Identified visual patterns driving engagement

# Visualization

Power BI dashboards for business stakeholders

# 📊 Key Insights

Logo-visible images showed ~25–30% higher engagement in Fashion & FMCG brands

Tech brands benefited more from product-focused visuals than logo-heavy imagery

Overcrowded images reduced engagement despite logo presence

Lifestyle context (people + product) outperformed isolated product shots
