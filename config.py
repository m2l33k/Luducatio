import os

# ===================================
# Configuration des chemins de fichiers
# ===================================
# Chemin vers les images du plateau d'échecs pour la détection
IMAGE_FOLDER = os.path.join(os.getcwd(), 'data', 'chess_board_images')

# Chemin vers les datasets de mouvements et de prédictions
MOVES_DATASET_PATH = os.path.join(os.getcwd(), 'data', 'moves_dataset', 'moves.csv')

# Chemin vers les annotations pour l'apprentissage supervisé
ANNOTATIONS_PATH = os.path.join(os.getcwd(), 'data', 'annotations')

# Chemin vers les modèles IA sauvegardés
MODEL_PATH = os.path.join(os.getcwd(), 'src', 'model', 'chess_model.h5')

# Chemin vers les données de consommation énergétique
ENERGY_DATA_PATH = os.path.join(os.getcwd(), 'data', 'energy_data', 'energy_usage.csv')

# ===================================
# Configuration des paramètres du modèle IA
# ===================================
# Paramètres pour l'entraînement du modèle
MODEL_PARAMS = {
    'epochs': 50,               # Nombre d'époques pour l'entraînement du modèle
    'batch_size': 32,           # Taille du lot pour l'entraînement
    'learning_rate': 0.001,     # Taux d'apprentissage
    'optimizer': 'adam',        # Optimiseur à utiliser pour l'entraînement
}

# ===================================
# Configuration du robot SCARA
# ===================================
# Paramètres du bras SCARA pour le contrôle du robot
ROBOT_PARAMS = {
    'arm_length': [200, 200],   # Longueur des bras du robot (en mm)
    'speed': 1.0,               # Vitesse des mouvements du bras (1.0 = vitesse normale)
    'max_torque': 10.0,         # Couple maximal que le robot peut exercer (en Nm)
    'angle_limits': [0, 180],   # Limites d'angle des joints (en degrés)
}

# ===================================
# Configuration de l'optimisation énergétique
# ===================================
# Paramètres pour l'optimisation de la consommation énergétique
ENERGY_OPTIMIZATION_PARAMS = {
    'solar_panel_efficiency': 0.85,   # Efficacité des panneaux solaires
    'battery_capacity': 100,          # Capacité de la batterie en Wh
    'power_consumption_rate': 10,     # Consommation énergétique du robot en W
}

# ===================================
# Configuration du flux de jeu (Échecs)
# ===================================
# Paramètres du jeu d'échecs
CHESS_GAME_PARAMS = {
    'time_limit': 10,               # Limite de temps par mouvement (en secondes)
    'difficulty': 'medium',         # Niveau de difficulté ('easy', 'medium', 'hard')
    'ai_play_style': 'defensive',   # Style de jeu de l'IA ('aggressive', 'defensive', 'balanced')
}

# ===================================
# Configuration de la caméra et du traitement d'image
# ===================================
# Paramètres pour la capture d'image du plateau d'échecs
CAMERA_PARAMS = {
    'camera_index': 0,             # Index de la caméra (0 pour la caméra par défaut)
    'frame_width': 640,            # Largeur de l'image capturée
    'frame_height': 480,           # Hauteur de l'image capturée
    'image_resolution': (640, 480),  # Résolution de l'image pour le traitement
}

# ===================================
# Configuration de l'interface utilisateur
# ===================================
# Paramètres pour l'interface utilisateur (si nécessaire)
UI_PARAMS = {
    'show_feedback': True,         # Afficher les retours en temps réel pendant le jeu
    'display_predictions': True,   # Afficher les prédictions du mouvement de l'IA
}

# ===================================
# Paramètres supplémentaires
# ===================================
# Paramètres pour les logs et la gestion des erreurs
LOGGING_PARAMS = {
    'log_file': os.path.join(os.getcwd(), 'logs', 'luducatio.log'),  # Fichier de log
    'log_level': 'INFO',                # Niveau de log (DEBUG, INFO, WARNING, ERROR)
}

# ===================================
# Configuration générale
# ===================================
# Paramètres généraux pour le projet
GENERAL_CONFIG = {
    'project_name': 'Luducatio',      # Nom du projet
    'version': '1.0',                 # Version du projet
    'debug_mode': False,              # Mode débogage activé ou non
}
