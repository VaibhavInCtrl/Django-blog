a
    ��`�  �                   @   sB   d dl mZ d dlmZmZ d dlZd dlZG dd� dej�ZdS )�    )�settings)�
migrations�modelsNc                   @   s�   e Zd ZdZe�ej�gZej	dde
jddddd�fde
jdd	�fd
e
�� fde
jejjjd�fde
jejj
jjejd�fgd�gZdS )�	MigrationT�Post�idF�ID)�auto_created�primary_key�	serialize�verbose_name�title�d   )�
max_length�content�date_posted)�default�author)�	on_delete�to)�name�fieldsN)�__name__�
__module__�__qualname__�initialr   �swappable_dependencyr   �AUTH_USER_MODEL�dependencies�CreateModelr   �BigAutoField�	CharField�	TextField�DateTimeField�django�utils�timezone�now�
ForeignKey�db�deletion�CASCADE�
operations� r-   r-   �\/Users/vaibhav_iitd24/Desktop/practice projects/coreyproject/blog/migrations/0001_initial.pyr   	   s   
�
���r   )	�django.confr   �	django.dbr   r   �django.db.models.deletionr$   Zdjango.utils.timezoner   r-   r-   r-   r.   �<module>   s   