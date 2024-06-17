// src/components/ProductoList.js

import React, { useState, useEffect } from 'react';
import api from '../api';

const ProductoList = () => {
    const [productos, setProductos] = useState([]);

    useEffect(() => {
        fetchProductos();
    }, []);

    const fetchProductos = async () => {
        try {
            const response = await api.get('productos/');
            setProductos(response.data);
        } catch (error) {
            console.error("Error fetching productos", error);
        }
    };

    const getUniqueImageUrl = (imagenUrl) => {
        return `${imagenUrl}?${new Date().getTime()}`;
    };

    return (
        <div>
            <h2>Lista de Productos</h2>
            <ul>
                {productos.map((producto) => (
                    <li key={producto.id}>
                        {producto.nombre} - ${producto.precio}
                        {producto.imagen && (
                            <img 
                                src={getUniqueImageUrl(`http://localhost:8000${producto.imagen}`)} 
                                alt={producto.nombre} 
                                style={{ width: '100px', height: '100px' }} 
                            />
                        )}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ProductoList;
