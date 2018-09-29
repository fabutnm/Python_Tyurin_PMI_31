from VkAPI import VkAPI


def main():
    id1 = 97039460
    id2 = 182017030
    q = VkAPI.my_friends_get_mutual(id1, id2)
    VkAPI.user_info_by_id(q)

if __name__ == '__main__':
    main()
