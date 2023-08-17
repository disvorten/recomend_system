
�6root"_tf_keras_network*�6{"name": "model", "trainable": true, "expects_training_arg": true, "dtype": "float32", "batch_input_shape": null, "must_restore_from_config": false, "preserve_input_structure_in_config": false, "autocast": false, "class_name": "Functional", "config": {"name": "model", "trainable": true, "layers": [{"class_name": "InputLayer", "config": {"batch_input_shape": {"class_name": "__tuple__", "items": [null, 1]}, "dtype": "float32", "sparse": false, "ragged": false, "name": "Book-Input"}, "name": "Book-Input", "inbound_nodes": []}, {"class_name": "InputLayer", "config": {"batch_input_shape": {"class_name": "__tuple__", "items": [null, 1]}, "dtype": "float32", "sparse": false, "ragged": false, "name": "User-Input"}, "name": "User-Input", "inbound_nodes": []}, {"class_name": "Embedding", "config": {"name": "Book-Embedding", "trainable": true, "dtype": "float32", "batch_input_shape": {"class_name": "__tuple__", "items": [null, null]}, "input_dim": 10001, "output_dim": 5, "embeddings_initializer": {"class_name": "RandomUniform", "config": {"minval": -0.05, "maxval": 0.05, "seed": null}}, "embeddings_regularizer": null, "activity_regularizer": null, "embeddings_constraint": null, "mask_zero": false, "input_length": null}, "name": "Book-Embedding", "inbound_nodes": [[["Book-Input", 0, 0, {}]]]}, {"class_name": "Embedding", "config": {"name": "User-Embedding", "trainable": true, "dtype": "float32", "batch_input_shape": {"class_name": "__tuple__", "items": [null, null]}, "input_dim": 53425, "output_dim": 5, "embeddings_initializer": {"class_name": "RandomUniform", "config": {"minval": -0.05, "maxval": 0.05, "seed": null}}, "embeddings_regularizer": null, "activity_regularizer": null, "embeddings_constraint": null, "mask_zero": false, "input_length": null}, "name": "User-Embedding", "inbound_nodes": [[["User-Input", 0, 0, {}]]]}, {"class_name": "Flatten", "config": {"name": "Flatten-Books", "trainable": true, "dtype": "float32", "data_format": "channels_last"}, "name": "Flatten-Books", "inbound_nodes": [[["Book-Embedding", 0, 0, {}]]]}, {"class_name": "Flatten", "config": {"name": "Flatten-Users", "trainable": true, "dtype": "float32", "data_format": "channels_last"}, "name": "Flatten-Users", "inbound_nodes": [[["User-Embedding", 0, 0, {}]]]}, {"class_name": "Dot", "config": {"name": "Dot-Product", "trainable": true, "dtype": "float32", "axes": 1, "normalize": false}, "name": "Dot-Product", "inbound_nodes": [[["Flatten-Books", 0, 0, {}], ["Flatten-Users", 0, 0, {}]]]}], "input_layers": [["User-Input", 0, 0], ["Book-Input", 0, 0]], "output_layers": [["Dot-Product", 0, 0]]}, "shared_object_id": 9, "input_spec": [{"class_name": "InputSpec", "config": {"dtype": null, "shape": {"class_name": "__tuple__", "items": [null, 1]}, "ndim": 2, "max_ndim": null, "min_ndim": null, "axes": {}}}, {"class_name": "InputSpec", "config": {"dtype": null, "shape": {"class_name": "__tuple__", "items": [null, 1]}, "ndim": 2, "max_ndim": null, "min_ndim": null, "axes": {}}}], "build_input_shape": [{"class_name": "TensorShape", "items": [null, 1]}, {"class_name": "TensorShape", "items": [null, 1]}], "is_graph_network": true, "full_save_spec": {"class_name": "__tuple__", "items": [[[{"class_name": "TypeSpec", "type_spec": "tf.TensorSpec", "serialized": [{"class_name": "TensorShape", "items": [null, 1]}, "float32", "User-Input"]}, {"class_name": "TypeSpec", "type_spec": "tf.TensorSpec", "serialized": [{"class_name": "TensorShape", "items": [null, 1]}, "float32", "Book-Input"]}]], {}]}, "save_spec": [{"class_name": "TypeSpec", "type_spec": "tf.TensorSpec", "serialized": [{"class_name": "TensorShape", "items": [null, 1]}, "float32", "User-Input"]}, {"class_name": "TypeSpec", "type_spec": "tf.TensorSpec", "serialized": [{"class_name": "TensorShape", "items": [null, 1]}, "float32", "Book-Input"]}], "keras_version": "2.13.1", "backend": "tensorflow", "model_config": {"class_name": "Functional", "config": {"name": "model", "trainable": true, "layers": [{"class_name": "InputLayer", "config": {"batch_input_shape": {"class_name": "__tuple__", "items": [null, 1]}, "dtype": "float32", "sparse": false, "ragged": false, "name": "Book-Input"}, "name": "Book-Input", "inbound_nodes": [], "shared_object_id": 0}, {"class_name": "InputLayer", "config": {"batch_input_shape": {"class_name": "__tuple__", "items": [null, 1]}, "dtype": "float32", "sparse": false, "ragged": false, "name": "User-Input"}, "name": "User-Input", "inbound_nodes": [], "shared_object_id": 1}, {"class_name": "Embedding", "config": {"name": "Book-Embedding", "trainable": true, "dtype": "float32", "batch_input_shape": {"class_name": "__tuple__", "items": [null, null]}, "input_dim": 10001, "output_dim": 5, "embeddings_initializer": {"class_name": "RandomUniform", "config": {"minval": -0.05, "maxval": 0.05, "seed": null}, "shared_object_id": 2}, "embeddings_regularizer": null, "activity_regularizer": null, "embeddings_constraint": null, "mask_zero": false, "input_length": null}, "name": "Book-Embedding", "inbound_nodes": [[["Book-Input", 0, 0, {}]]], "shared_object_id": 3}, {"class_name": "Embedding", "config": {"name": "User-Embedding", "trainable": true, "dtype": "float32", "batch_input_shape": {"class_name": "__tuple__", "items": [null, null]}, "input_dim": 53425, "output_dim": 5, "embeddings_initializer": {"class_name": "RandomUniform", "config": {"minval": -0.05, "maxval": 0.05, "seed": null}, "shared_object_id": 4}, "embeddings_regularizer": null, "activity_regularizer": null, "embeddings_constraint": null, "mask_zero": false, "input_length": null}, "name": "User-Embedding", "inbound_nodes": [[["User-Input", 0, 0, {}]]], "shared_object_id": 5}, {"class_name": "Flatten", "config": {"name": "Flatten-Books", "trainable": true, "dtype": "float32", "data_format": "channels_last"}, "name": "Flatten-Books", "inbound_nodes": [[["Book-Embedding", 0, 0, {}]]], "shared_object_id": 6}, {"class_name": "Flatten", "config": {"name": "Flatten-Users", "trainable": true, "dtype": "float32", "data_format": "channels_last"}, "name": "Flatten-Users", "inbound_nodes": [[["User-Embedding", 0, 0, {}]]], "shared_object_id": 7}, {"class_name": "Dot", "config": {"name": "Dot-Product", "trainable": true, "dtype": "float32", "axes": 1, "normalize": false}, "name": "Dot-Product", "inbound_nodes": [[["Flatten-Books", 0, 0, {}], ["Flatten-Users", 0, 0, {}]]], "shared_object_id": 8}], "input_layers": [["User-Input", 0, 0], ["Book-Input", 0, 0]], "output_layers": [["Dot-Product", 0, 0]]}}, "training_config": {"loss": "mean_squared_error", "metrics": null, "weighted_metrics": null, "loss_weights": null, "optimizer_config": {"class_name": "Custom>Adam", "config": {"name": "Adam", "weight_decay": null, "clipnorm": null, "global_clipnorm": null, "clipvalue": null, "use_ema": false, "ema_momentum": 0.99, "ema_overwrite_frequency": null, "jit_compile": false, "is_legacy_optimizer": false, "learning_rate": 0.0010000000474974513, "beta_1": 0.9, "beta_2": 0.999, "epsilon": 1e-07, "amsgrad": false}}}}2
�root.layer-0"_tf_keras_input_layer*�{"class_name": "InputLayer", "name": "Book-Input", "dtype": "float32", "sparse": false, "ragged": false, "batch_input_shape": {"class_name": "__tuple__", "items": [null, 1]}, "config": {"batch_input_shape": {"class_name": "__tuple__", "items": [null, 1]}, "dtype": "float32", "sparse": false, "ragged": false, "name": "Book-Input"}}2
�root.layer-1"_tf_keras_input_layer*�{"class_name": "InputLayer", "name": "User-Input", "dtype": "float32", "sparse": false, "ragged": false, "batch_input_shape": {"class_name": "__tuple__", "items": [null, 1]}, "config": {"batch_input_shape": {"class_name": "__tuple__", "items": [null, 1]}, "dtype": "float32", "sparse": false, "ragged": false, "name": "User-Input"}}2
�root.layer_with_weights-0"_tf_keras_layer*�{"name": "Book-Embedding", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": {"class_name": "__tuple__", "items": [null, null]}, "stateful": false, "must_restore_from_config": false, "preserve_input_structure_in_config": false, "autocast": false, "class_name": "Embedding", "config": {"name": "Book-Embedding", "trainable": true, "dtype": "float32", "batch_input_shape": {"class_name": "__tuple__", "items": [null, null]}, "input_dim": 10001, "output_dim": 5, "embeddings_initializer": {"class_name": "RandomUniform", "config": {"minval": -0.05, "maxval": 0.05, "seed": null}, "shared_object_id": 2}, "embeddings_regularizer": null, "activity_regularizer": null, "embeddings_constraint": null, "mask_zero": false, "input_length": null}, "inbound_nodes": [[["Book-Input", 0, 0, {}]]], "shared_object_id": 3, "build_input_shape": {"class_name": "TensorShape", "items": [null, 1]}}2
�root.layer_with_weights-1"_tf_keras_layer*�{"name": "User-Embedding", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": {"class_name": "__tuple__", "items": [null, null]}, "stateful": false, "must_restore_from_config": false, "preserve_input_structure_in_config": false, "autocast": false, "class_name": "Embedding", "config": {"name": "User-Embedding", "trainable": true, "dtype": "float32", "batch_input_shape": {"class_name": "__tuple__", "items": [null, null]}, "input_dim": 53425, "output_dim": 5, "embeddings_initializer": {"class_name": "RandomUniform", "config": {"minval": -0.05, "maxval": 0.05, "seed": null}, "shared_object_id": 4}, "embeddings_regularizer": null, "activity_regularizer": null, "embeddings_constraint": null, "mask_zero": false, "input_length": null}, "inbound_nodes": [[["User-Input", 0, 0, {}]]], "shared_object_id": 5, "build_input_shape": {"class_name": "TensorShape", "items": [null, 1]}}2
�root.layer-4"_tf_keras_layer*�{"name": "Flatten-Books", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "preserve_input_structure_in_config": false, "autocast": true, "class_name": "Flatten", "config": {"name": "Flatten-Books", "trainable": true, "dtype": "float32", "data_format": "channels_last"}, "inbound_nodes": [[["Book-Embedding", 0, 0, {}]]], "shared_object_id": 6, "input_spec": {"class_name": "InputSpec", "config": {"dtype": null, "shape": null, "ndim": null, "max_ndim": null, "min_ndim": 1, "axes": {}}, "shared_object_id": 12}, "build_input_shape": {"class_name": "TensorShape", "items": [null, 1, 5]}}2
�root.layer-5"_tf_keras_layer*�{"name": "Flatten-Users", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "preserve_input_structure_in_config": false, "autocast": true, "class_name": "Flatten", "config": {"name": "Flatten-Users", "trainable": true, "dtype": "float32", "data_format": "channels_last"}, "inbound_nodes": [[["User-Embedding", 0, 0, {}]]], "shared_object_id": 7, "input_spec": {"class_name": "InputSpec", "config": {"dtype": null, "shape": null, "ndim": null, "max_ndim": null, "min_ndim": 1, "axes": {}}, "shared_object_id": 13}, "build_input_shape": {"class_name": "TensorShape", "items": [null, 1, 5]}}2
�root.layer-6"_tf_keras_layer*�{"name": "Dot-Product", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "preserve_input_structure_in_config": false, "autocast": true, "class_name": "Dot", "config": {"name": "Dot-Product", "trainable": true, "dtype": "float32", "axes": 1, "normalize": false}, "inbound_nodes": [[["Flatten-Books", 0, 0, {}], ["Flatten-Users", 0, 0, {}]]], "shared_object_id": 8, "build_input_shape": [{"class_name": "TensorShape", "items": [null, 5]}, {"class_name": "TensorShape", "items": [null, 5]}]}2
�groot.keras_api.metrics.0"_tf_keras_metric*�{"class_name": "Mean", "name": "loss", "dtype": "float32", "config": {"name": "loss", "dtype": "float32"}, "shared_object_id": 14}2