create table users (
    id serial not null primary key,
    username varchar(255) not null,
    email varchar(255) not null,
    password varchar(255) not null
);

create table categories (
    id serial not null primary key,
    name varchar(255) not null
);

create table types (
    id serial not null primary key,
    name varchar(255) not null
);

create table products (
    id serial not null primary key,
    name varchar(255) not null,
    main_image varchar(255) not null,
    images varchar(255)[] not null,
    description text not null,
    short_description text not null,
    price decimal(10,2) not null,
    weight varchar(255) not null,
    dimensions varchar(255) not null,
    category_id int not null references categories(id)
);

create table card_font (
    id serial not null primary key,
    name varchar(255) not null,
    attachments varchar(255) not null
);

create table card_decorations (
    id serial not null primary key,
    name varchar(255) not null,
    attachments varchar(255) not null
);

create table cards (
    id serial not null primary key,
    name varchar(255) not null,
    front varchar(255) not null,
    back varchar(255) not null,
    price decimal(10,2) default 0.00 not null,
    user_id int not null references users(id)
);

create table carts (
    id serial not null primary key,
    type_id int not null references types(id),
    user_id int not null references users(id),
    product_id int references products(id),
    quantity int not null,
    card_id int references cards(id),
    created_time timestamp default now()
);

create table orders (
    id serial primary key,
    user_id int references users(id),
    amount decimal(10,2) not null,
    created_at timestamp default now()
);

create table order_details (
    id serial primary key,
    order_id int not null references orders(id),
    type_id int not null references types(id),
    product_id int references products(id),
    quantity int not null default 0,
    card_id int references cards(id),
    created_time timestamp default now()
);