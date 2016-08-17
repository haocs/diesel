BEGIN;
--
-- Create model Post
--
CREATE TABLE `blog_post` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `language` varchar(5) NOT NULL, `title` varchar(256) NOT NULL, `content` longtext NOT NULL, `created_timestamp` datetime(6) NOT NULL, `mod_timestamp` date NOT NULL, `privacy` varchar(10) NOT NULL, `deleted` bool NOT NULL, `del_timestamp` date NULL, `status` varchar(1) NOT NULL, `author_id` integer NOT NULL);
--
-- Create model Tag
--
CREATE TABLE `blog_tag` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(20) NOT NULL);
CREATE TABLE `blog_tag_posts` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `tag_id` integer NOT NULL, `post_id` integer NOT NULL);
ALTER TABLE `blog_post` ADD CONSTRAINT `blog_post_author_id_dd7a8485_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `blog_tag_posts` ADD CONSTRAINT `blog_tag_posts_tag_id_5f489887_fk_blog_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `blog_tag` (`id`);
ALTER TABLE `blog_tag_posts` ADD CONSTRAINT `blog_tag_posts_post_id_99049a47_fk_blog_post_id` FOREIGN KEY (`post_id`) REFERENCES `blog_post` (`id`);
ALTER TABLE `blog_tag_posts` ADD CONSTRAINT `blog_tag_posts_tag_id_3e2e54c9_uniq` UNIQUE (`tag_id`, `post_id`);

COMMIT;
